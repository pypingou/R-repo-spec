%global packname  trifield
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Some basic facilities for ternary fields and plots

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package contains routines to 1) project unity-summed triples to
unit-square doubles and vice versa, 2) make a grid of unity-summed triples
paired to doubles, 3) evaluate a function over the grid and 4) make simple
plots including ternary contour plots over a grid of values.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/trifield/html
%doc %{rlibdir}/trifield/DESCRIPTION
%{rlibdir}/trifield/R
%{rlibdir}/trifield/NAMESPACE
%{rlibdir}/trifield/help
%{rlibdir}/trifield/INDEX
%{rlibdir}/trifield/demo
%{rlibdir}/trifield/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora