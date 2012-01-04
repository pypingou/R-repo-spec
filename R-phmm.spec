%global packname  phmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Proportional Hazards Mixed-effects Model (PHMM)

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-lattice R-Matrix 

BuildRequires:    R-devel tex(latex) R-survival R-lattice R-Matrix 

%description
Fits proportional hazards model incorporating random effects using an EM
algorithm using Markov Chain Monte Carlo at E-step.

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
%doc %{rlibdir}/phmm/DESCRIPTION
%doc %{rlibdir}/phmm/doc
%doc %{rlibdir}/phmm/html
%{rlibdir}/phmm/help
%{rlibdir}/phmm/INDEX
%{rlibdir}/phmm/libs
%{rlibdir}/phmm/Meta
%{rlibdir}/phmm/R
%{rlibdir}/phmm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora