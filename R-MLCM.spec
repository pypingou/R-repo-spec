%global packname  MLCM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.9
Release:          1%{?dist}
Summary:          Maximum Likelihood Conjoint Measurement

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-utils R-base 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-utils R-base 

%description
Conjoint measurement is a psychophysical procedure in which stimulus pairs
are presented that vary along 2 or more dimensions and the observer is
required to compare the stimuli along one of them.  This package contains
functions to estimate the contribution of the n scales to the judgment by
a maximum likelihood method under several hypotheses of how the perceptual
dimensions interact.

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
%doc %{rlibdir}/MLCM/NEWS
%doc %{rlibdir}/MLCM/html
%doc %{rlibdir}/MLCM/DESCRIPTION
%{rlibdir}/MLCM/NAMESPACE
%{rlibdir}/MLCM/R
%{rlibdir}/MLCM/data
%{rlibdir}/MLCM/help
%{rlibdir}/MLCM/INDEX
%{rlibdir}/MLCM/Meta
%{rlibdir}/MLCM/ToDo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.9-1
- initial package for Fedora