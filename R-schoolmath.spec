%global packname  schoolmath
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Functions and datasets for math used in school

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions and datasets for math taught in school. A
main focus is set to prime-calculation

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
%doc %{rlibdir}/schoolmath/DESCRIPTION
%doc %{rlibdir}/schoolmath/html
%{rlibdir}/schoolmath/INDEX
%{rlibdir}/schoolmath/help
%{rlibdir}/schoolmath/data
%{rlibdir}/schoolmath/NAMESPACE
%{rlibdir}/schoolmath/R
%{rlibdir}/schoolmath/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora