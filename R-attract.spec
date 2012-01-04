%global packname  attract
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Methods to Find the Gene Expression Modules that Represent the Drivers of Kauffman's Attractor Landscape

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-AnnotationDbi R-KEGG.db R-limma R-cluster R-GOstats R-graphics R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-AnnotationDbi R-KEGG.db R-limma R-cluster R-GOstats R-graphics R-methods R-stats 

%description
This package contains the functions to find the gene expression modules
that represent the drivers of Kauffman's attractor landscape. The modules
are the core attractor pathways that discriminate between different cell
types of groups of interest. Each pathway has a set of synexpression
groups, which show transcriptionally-coordinated changes in gene

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