%global packname  psychotree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.12.1
Release:          1%{?dist}
Summary:          Recursive Partitioning Based on Psychometric Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.12-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-psychotools R-party R-strucchange R-modeltools 
Requires:         R-graphics R-stats R-psychotools R-sandwich 

BuildRequires:    R-devel tex(latex) R-stats R-psychotools R-party R-strucchange R-modeltools
BuildRequires:    R-graphics R-stats R-psychotools R-sandwich 


%description
Recursive partitioning based on psychometric models, employing the general
MOB algorithm (from package party) to obtain Bradley-Terry trees and Rasch

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.12.1-1
- initial package for Fedora