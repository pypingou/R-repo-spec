%global packname  GeneRegionScan
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          GeneRegionScan

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-Biostrings 
Requires:         R-Biobase R-affxparser R-RColorBrewer R-Biostrings 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-Biostrings
BuildRequires:    R-Biobase R-affxparser R-RColorBrewer R-Biostrings 


%description
A package with focus on analysis of discrete regions of the genome. This
package is useful for investigation of one or a few genes using Affymetrix
data, since it will extract probe level data using the Affymetrix Power
Tools application and wrap these data into a ProbeLevelSet. A
ProbeLevelSet directly extends the expressionSet, but includes additional
information about the sequence of each probe and the probe set it is
derived from. The package includes a number of functions used for plotting
these probe level data as a function of location along sequences of
mRNA-strands. This can be used for analysis of variable splicing, and is
especially well suited for use with exon-array data.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora