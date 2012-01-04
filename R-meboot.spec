%global packname  meboot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Maximum Entropy Bootstrap for Time Series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ConvergenceConcepts R-dynlm R-kinship R-survival R-splines R-nlme R-lattice R-plm R-zoo 


BuildRequires:    R-devel tex(latex) R-ConvergenceConcepts R-dynlm R-kinship R-survival R-splines R-nlme R-lattice R-plm R-zoo



%description
This package performs maximum entropy density based dependent data
bootstrap. An algorithm is provided to create a population of time series
(ensemble) without assuming stationarity. The reference paper (Vinod,
H.D., 2004) explains how the algorithm satisfies the ergodic theorem and
the central limit theorem.

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
%changelog
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora