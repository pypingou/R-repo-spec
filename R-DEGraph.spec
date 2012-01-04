%global packname  DEGraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Two-sample tests on a graph

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.utils 

BuildRequires:    R-devel tex(latex) R-R.utils 

%description
DEGraph implements recent hypothesis testing methods which directly assess
whether a particular gene network is differentially expressed between two
conditions. This is to be contrasted with the more classical two-step
approaches which first test individual genes, then test gene sets for
enrichment in differentially expressed genes. These recent methods take
into account the topology of the network to yield more powerful detection
procedures. DEGraph provides methods to easily test all KEGG pathways for
differential expression on any gene expression data set and tools to
visualize the results.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora