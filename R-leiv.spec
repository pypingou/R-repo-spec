%global packname  leiv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Bivariate linear errors-in-variables estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
Estimate the slope and intercept of a bivariate linear relationship by
calculating a posterior density that is invariant to interchange and
scaling of the coordinates.

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
%doc %{rlibdir}/leiv/NEWS
%doc %{rlibdir}/leiv/html
%doc %{rlibdir}/leiv/CITATION
%doc %{rlibdir}/leiv/DESCRIPTION
%doc %{rlibdir}/leiv/doc
%{rlibdir}/leiv/INDEX
%{rlibdir}/leiv/NAMESPACE
%{rlibdir}/leiv/help
%{rlibdir}/leiv/Meta
%{rlibdir}/leiv/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora