%global packname  vwr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Useful functions for visual word recognition research

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RecordLinkage R-lattice R-latticeExtra 


BuildRequires:    R-devel tex(latex) R-RecordLinkage R-lattice R-latticeExtra



%description
Functions and data for use in visual word recognition research: Supports
computation of neighbors (Hamming and Levenshtein distances), average
distances to neighbors (e.g., OLD20), and Coltheart's N. Also includes the
LD1NN algorithm to detect bias in the composition of a lexical decision
task. Most of the functions support parallel execution. Supplies wordlists
for several languages.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora