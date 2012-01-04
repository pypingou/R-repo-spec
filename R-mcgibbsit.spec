%global packname  mcgibbsit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Warnes and Raftery's MCGibbsit MCMC diagnostic

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-coda 

BuildRequires:    R-devel tex(latex) R-coda 

%description
mcgibbsit provides an implementation of Warnes & Raftery's MCGibbsit
run-length diagnostic for a set of (not-necessarily independent) MCMC
sampers.  It combines the estimate error-bounding approach of Raftery and
Lewis with evaulate between verses within chain approach of Gelman and

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
%doc %{rlibdir}/mcgibbsit/DESCRIPTION
%doc %{rlibdir}/mcgibbsit/NEWS
%doc %{rlibdir}/mcgibbsit/html
%{rlibdir}/mcgibbsit/ChangeLog
%{rlibdir}/mcgibbsit/R
%{rlibdir}/mcgibbsit/INDEX
%{rlibdir}/mcgibbsit/Meta
%{rlibdir}/mcgibbsit/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora