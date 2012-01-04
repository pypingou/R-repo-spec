%global packname  SDisc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24
Release:          1%{?dist}
Summary:          Integrated methodology for the identification of homogeneous subtypes in data

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mclust R-stats R-utils R-RColorBrewer R-abind R-xtable R-digest R-e1071 R-snow R-SparseM 

BuildRequires:    R-devel tex(latex) R-mclust R-stats R-utils R-RColorBrewer R-abind R-xtable R-digest R-e1071 R-snow R-SparseM 

%description
Tools and methods to identify homogeneous subtypes in data by cluster
analysis; includes methods for data pre-processing, repeated cluster
analysis, model selection, model reliability and reproducibility
assessment, subtype characterization and validation.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24-1
- initial package for Fedora