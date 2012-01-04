%global packname  triangle
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Provides the standard distribution functions for the triangle distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Provides the "r, q, p, and d" distribution functions for the triangle

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
%doc %{rlibdir}/triangle/DESCRIPTION
%doc %{rlibdir}/triangle/html
%{rlibdir}/triangle/INDEX
%{rlibdir}/triangle/NAMESPACE
%{rlibdir}/triangle/help
%{rlibdir}/triangle/Meta
%{rlibdir}/triangle/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora