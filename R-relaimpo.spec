%global packname  relaimpo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Relative importance of regressors in linear models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-boot R-survey R-methods R-mitools R-corpcor 

BuildRequires:    R-devel tex(latex) R-MASS R-boot R-survey R-methods R-mitools R-corpcor 

%description
relaimpo provides several metrics for assessing relative importance in
linear models. These can be printed, plotted and bootstrapped. The
recommended metric is lmg, which provides a decomposition of the model
explained variance into non-negative contributions. There is a version of
this package available that additionally provides a new and also
recommended metric called pmvd. If you are a non-US user, you can download
this extended version from Ulrike Groempings web site.

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
%doc %{rlibdir}/relaimpo/NEWS
%doc %{rlibdir}/relaimpo/html
%doc %{rlibdir}/relaimpo/DESCRIPTION
%doc %{rlibdir}/relaimpo/CITATION
%{rlibdir}/relaimpo/INDEX
%{rlibdir}/relaimpo/NAMESPACE
%{rlibdir}/relaimpo/help
%{rlibdir}/relaimpo/R
%{rlibdir}/relaimpo/Meta
%{rlibdir}/relaimpo/LICENSE

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora