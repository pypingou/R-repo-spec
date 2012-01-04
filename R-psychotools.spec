%global packname  psychotools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Infrastructure for Psychometric Modeling

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Infrastructure for psychometric modeling such as data classes (e.g., for
paired comparisons) and basic model fitting functions (e.g., for Rasch and
Bradley-Terry models). Intended especially as a common building block for
fitting psychometric mixture models in package "psychomix" and
psychometric tree models in package "psychotree".

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
%doc %{rlibdir}/psychotools/NEWS
%doc %{rlibdir}/psychotools/html
%doc %{rlibdir}/psychotools/DESCRIPTION
%{rlibdir}/psychotools/R
%{rlibdir}/psychotools/INDEX
%{rlibdir}/psychotools/help
%{rlibdir}/psychotools/Meta
%{rlibdir}/psychotools/data
%{rlibdir}/psychotools/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora