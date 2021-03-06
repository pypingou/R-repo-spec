%global packname  GeneAnswers
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Integrated Interpretation of Genes

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-igraph R-RCurl R-annotate R-Biobase R-methods R-XML R-RSQLite R-MASS R-rgl R-Heatplus R-RColorBrewer 
Requires:         R-graph R-Rgraphviz R-RBGL R-annotate 

BuildRequires:    R-devel tex(latex) R-igraph R-RCurl R-annotate R-Biobase R-methods R-XML R-RSQLite R-MASS R-rgl R-Heatplus R-RColorBrewer
BuildRequires:    R-graph R-Rgraphviz R-RBGL R-annotate 


%description
GeneAnswers provides an integrated tool for biological or medical
interpretation of the given one or more groups of genes by means of
statistical test.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora