%global packname  Rmagpie
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          MicroArray Gene-expression-based Program In Error rate estimation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-Biobase R-e1071 R-graphics R-grDevices R-kernlab R-methods R-pamr R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-Biobase R-e1071 R-graphics R-grDevices R-kernlab R-methods R-pamr R-stats R-utils 


%description
Microarray Classification is designed for both biologists and
statisticians. It offers the ability to train a classifier on a labelled
microarray dataset and to then use that classifier to predict the class of
new observations. A range of modern classifiers are available, including
support vector machines (SVMs), nearest shrunken centroids (NSCs)...
Advanced methods are provided to estimate the predictive error rate and to
report the  subset of genes which appear essential in discriminating
between classes.

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
%doc %{rlibdir}/Rmagpie/html
%doc %{rlibdir}/Rmagpie/doc
%doc %{rlibdir}/Rmagpie/DESCRIPTION
%{rlibdir}/Rmagpie/NAMESPACE
%{rlibdir}/Rmagpie/Meta
%{rlibdir}/Rmagpie/R
%{rlibdir}/Rmagpie/demo
%{rlibdir}/Rmagpie/data
%{rlibdir}/Rmagpie/INDEX
%{rlibdir}/Rmagpie/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora