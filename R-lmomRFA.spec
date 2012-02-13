%global packname  lmomRFA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4
Release:          1%{dist}
Summary:          Regional frequency analysis using L-moments

Group:            Applications/Engineering 
License:          Common Public License Version 1.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lmom 

BuildRequires:    R-devel tex(latex) R-lmom 

%description
Functions for regional frequency analysis using the methods of J. R. M.
Hosking and J. R. Wallis (1997), "Regional frequency analysis: an approach
based on L-moments".

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
%doc %{rlibdir}/lmomRFA/NEWS
%doc %{rlibdir}/lmomRFA/html
%doc %{rlibdir}/lmomRFA/CITATION
%doc %{rlibdir}/lmomRFA/DESCRIPTION
%{rlibdir}/lmomRFA/Meta
%{rlibdir}/lmomRFA/libs
%{rlibdir}/lmomRFA/R
%{rlibdir}/lmomRFA/NAMESPACE
%{rlibdir}/lmomRFA/help
%{rlibdir}/lmomRFA/LICENSE
%{rlibdir}/lmomRFA/data
%{rlibdir}/lmomRFA/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4-1
- Update to version 2.4

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora