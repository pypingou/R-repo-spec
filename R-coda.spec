%global packname  coda
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.14.6
Release:          1%{?dist}
Summary:          Output analysis and diagnostics for MCMC

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.14-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Output analysis and diagnostics for Markov Chain Monte Carlo simulations.

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
%doc %{rlibdir}/coda/DESCRIPTION
%doc %{rlibdir}/coda/CITATION
%doc %{rlibdir}/coda/html
%{rlibdir}/coda/Meta
%{rlibdir}/coda/data
%{rlibdir}/coda/help
%{rlibdir}/coda/INDEX
%{rlibdir}/coda/R
%{rlibdir}/coda/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.14.6-1
- initial package for Fedora