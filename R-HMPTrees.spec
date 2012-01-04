%global packname  HMPTrees
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Statistical Object Oriented Data Analysis of RDP-based Taxonomic trees from Human Microbiome Data: Modeling, Visualization, and Two-Group Comparison

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ape 


BuildRequires:    R-devel tex(latex) R-ape



%description
In this package, we introduce Object Oriented Data Analysis (OODA) methods
to analyze Human Microbiome taxonomic trees directly. We provide tools to
model, compare, and visualize populations of taxonomic tree objects. In
particular, using a unimodal probability measure in the set of trees, we
provide procedures to compute the MLE of the central tree and the LRT
statistics for comparing the distributions of two metagenomic populations.
Our procedures have been developed to support parallel computations for
comparing two groups.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora