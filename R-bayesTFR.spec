%global packname  bayesTFR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Bayesian Fertility Projection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-coda 


BuildRequires:    R-devel tex(latex) R-mvtnorm R-coda



%description
Making probabilistic projections of total fertility rate for all countries
of the world, using a Bayesian hierarchical model.

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
%doc %{rlibdir}/bayesTFR/html
%doc %{rlibdir}/bayesTFR/DESCRIPTION
%doc %{rlibdir}/bayesTFR/CITATION
%{rlibdir}/bayesTFR/data
%{rlibdir}/bayesTFR/INDEX
%{rlibdir}/bayesTFR/R
%{rlibdir}/bayesTFR/help
%{rlibdir}/bayesTFR/NAMESPACE
%{rlibdir}/bayesTFR/ex-data
RPM build errors:
%{rlibdir}/bayesTFR/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora