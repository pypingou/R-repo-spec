%global packname  ttime
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Translate Neurodevelopmental Event Timing Across Species

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-pvclust 

BuildRequires:    R-devel tex(latex) R-pvclust 

%description
Translate neurodevelopmental event timing across species. Predict unknown
event timings and investigate phylogenetic proximity by hierarchical
clustering of the known and predicted event timings.

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
%doc %{rlibdir}/ttime/html
%doc %{rlibdir}/ttime/DESCRIPTION
%{rlibdir}/ttime/help
%{rlibdir}/ttime/data
%{rlibdir}/ttime/Meta
%{rlibdir}/ttime/R
%{rlibdir}/ttime/INDEX
%{rlibdir}/ttime/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora