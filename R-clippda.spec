%global packname  clippda
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          A package for the clinical proteomic profiling data analysis

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-limma R-statmod R-rgl R-lattice R-scatterplot3d R-graphics R-grDevices R-stats R-utils R-Biobase R-tools R-methods 


BuildRequires:    R-devel tex(latex) R-limma R-statmod R-rgl R-lattice R-scatterplot3d R-graphics R-grDevices R-stats R-utils R-Biobase R-tools R-methods



%description
Methods for the nalysis of data from clinical proteomic profiling studies.
The focus is on the studies of human subjects, 	which are often
observational case-control by design and have 	technical replicates. A
method for sample size determination for 	planning these studies is
proposed. It incorporates routines for 	adjusting for the expected
heterogeneities and imbalances in the 	data and the within-sample
replicate correlations.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora