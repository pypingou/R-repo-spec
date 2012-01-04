%global packname  intervals
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.13.3
Release:          1%{?dist}
Summary:          Tools for working with points and intervals

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Tools for working with and comparing sets of points and intervals.

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
%doc %{rlibdir}/intervals/html
%doc %{rlibdir}/intervals/NEWS
%doc %{rlibdir}/intervals/DESCRIPTION
%doc %{rlibdir}/intervals/doc
%{rlibdir}/intervals/libs
%{rlibdir}/intervals/data
%{rlibdir}/intervals/R
%{rlibdir}/intervals/help
%{rlibdir}/intervals/Meta
%{rlibdir}/intervals/NAMESPACE
%{rlibdir}/intervals/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.13.3-1
- initial package for Fedora