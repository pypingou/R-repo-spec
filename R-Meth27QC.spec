%global packname  Meth27QC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Meth27QC: sample quality analysis, and sample control analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gplots R-tcltk 


BuildRequires:    R-devel tex(latex) R-gplots R-tcltk



%description
Meth27QC is a tool for analyzing Illumina Infinium HumanMethylation27
BeadChip Data and generating QC reports. This package allows users quickly
assess data quality of the Assay. Users can evaluate the data quality in
the way that Illumina GenomeStudio/BeadStudio recommended based on the
control probes. The package reads files exported from
GenomeStudio/BeadStudio software, generating intensity and standard
deviation plots grouped by the types of the control probes. Meth27 carries
40 control probes for staining, hybridization, target removal, extension,
bisulfite conversion, specificity, negative and non-polymorphic controls.
Details of those control probes can be found in the Infinium Assay for
Methylation Protocol Guide from Illumina.We also used the other
non-control probes to plot intensity of detected genes, signal average for
green and red. Outliers can be identified.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora