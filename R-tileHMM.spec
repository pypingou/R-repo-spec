%global packname  tileHMM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Hidden Markov Models for ChIP-on-Chip Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package provides methods and classes to build HMMs that are suitable
for the analysis of ChIP-on-chip data. The provided parameter estimation
methods include the Baum-Welch algorithm and Viterbi training as well as a
combination of both.

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
%doc %{rlibdir}/tileHMM/DESCRIPTION
%doc %{rlibdir}/tileHMM/COPYING
%doc %{rlibdir}/tileHMM/CITATION
%doc %{rlibdir}/tileHMM/doc
%doc %{rlibdir}/tileHMM/html
%{rlibdir}/tileHMM/NAMESPACE
%{rlibdir}/tileHMM/INDEX
%{rlibdir}/tileHMM/Meta
%{rlibdir}/tileHMM/help
%{rlibdir}/tileHMM/data
%{rlibdir}/tileHMM/R
RPM build errors:
%{rlibdir}/tileHMM/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora