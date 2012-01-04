%global packname  BioSeqClass
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Classification for Biological Sequences

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biostrings R-ipred R-e1071 R-klaR R-randomForest R-class R-tree R-nnet R-rpart R-party R-foreign R-Biobase R-utils R-stats R-grDevices 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biostrings R-ipred R-e1071 R-klaR R-randomForest R-class R-tree R-nnet R-rpart R-party R-foreign R-Biobase R-utils R-stats R-grDevices 


%description
Extracting Features from Biological Sequences and Building Classification

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora