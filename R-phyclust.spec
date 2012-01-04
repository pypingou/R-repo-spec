%global packname  phyclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.10
Release:          1%{?dist}
Summary:          Phylogenetic Clustering (Phyloclustering)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ape 


BuildRequires:    R-devel tex(latex) R-ape



%description
Phylogenetic clustering (phyloclustering) is an evolutionary Continuous
Time Markov Chain model-based approach to identify population structure
from molecular data without assuming linkage equilibrium. It provides a
convenient implementation of phyloclustering for DNA and SNP data, capable
of clustering individuals into subpopulations and identifying molecular
sequences representative of those subpopulations. It is designed in C for
performance, interfaced with R for visualization, and incorporates other
popular open source software, ms, seq-gen and Hap-Clustering for
simulating data and additional analyses. See the phyclust website for more
information, documentations and examples.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.10-1
- initial package for Fedora