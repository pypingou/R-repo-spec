%global packname  leaps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.9
Release:          1%{?dist}
Summary:          regression subset selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Regression subset selection including exhaustive search

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
%doc %{rlibdir}/leaps/DESCRIPTION
%doc %{rlibdir}/leaps/html
%doc %{rlibdir}/leaps/NEWS
%{rlibdir}/leaps/libs
%{rlibdir}/leaps/Meta
%{rlibdir}/leaps/NAMESPACE
%{rlibdir}/leaps/R
%{rlibdir}/leaps/INDEX
%{rlibdir}/leaps/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.9-1
- initial package for Fedora