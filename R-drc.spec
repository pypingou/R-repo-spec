%global packname  drc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Analysis of dose-response curves

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-alr3 R-gtools R-lattice R-magic R-MASS R-nlme R-plotrix R-methods R-stats4 

BuildRequires:    R-devel tex(latex) R-alr3 R-gtools R-lattice R-magic R-MASS R-nlme R-plotrix R-methods R-stats4 

%description
Analysis of one or multiple curves with focus on concentration-response,
dose-response and time-response curves used, for example in biology,
environmental sciences, medicine, pharmacology, toxicology.

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
%doc %{rlibdir}/drc/NEWS
%doc %{rlibdir}/drc/html
%doc %{rlibdir}/drc/DESCRIPTION
%doc %{rlibdir}/drc/LICENCE
%doc %{rlibdir}/drc/CITATION
%{rlibdir}/drc/Meta
%{rlibdir}/drc/help
%{rlibdir}/drc/R
%{rlibdir}/drc/data
%{rlibdir}/drc/NAMESPACE
%{rlibdir}/drc/INDEX

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.1-1
- initial package for Fedora