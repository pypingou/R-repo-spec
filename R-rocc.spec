%global packname  rocc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          ROC based classification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ROCR 


BuildRequires:    R-devel tex(latex) R-ROCR



%description
Functions for a classification method based on receiver operating
characteristics (ROC). Briefly, features are selected according to their
ranked AUC value in the training set. The selected features are merged by
the mean value to form a metagene. The samples are ranked by their
metagene value and the metagene threshold that has the highest accuracy in
splitting the training samples is determined. A new sample is classified
by its metagene value relative to the threshold. In the first place, the
package is aimed at two class problems in gene expression data, but might
also apply to other problems.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora