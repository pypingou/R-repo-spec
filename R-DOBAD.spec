%global packname  DOBAD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Analysis of Discretely Observed linear Birth-And-Death(-and-immigration) Markov Chains

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lattice R-numDeriv 

BuildRequires:    R-devel tex(latex) R-methods R-lattice R-numDeriv 

%description
Frequentist (EM) and Bayesian (MCMC) Methods for Inference of
Birth-Death-Immigration Markov Chains

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
%doc %{rlibdir}/DOBAD/doc
%doc %{rlibdir}/DOBAD/html
%doc %{rlibdir}/DOBAD/DESCRIPTION
%{rlibdir}/DOBAD/INDEX
%{rlibdir}/DOBAD/R
%{rlibdir}/DOBAD/NAMESPACE
RPM build errors:
%{rlibdir}/DOBAD/LICENSE
%{rlibdir}/DOBAD/Meta
%{rlibdir}/DOBAD/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora