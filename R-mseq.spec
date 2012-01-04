%global packname  mseq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Modeling non-uniformity in short-read rates in RNA-Seq data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gbm 

BuildRequires:    R-devel tex(latex) R-gbm 

%description
This package implements all the methods in the paper "Modeling
non-uniformity in short-read rates in RNA-Seq data". Especially, it
implements both the iterative glm procedure for the Poisson linear model
and the training procedure of the MART model. The cross-validation for
both of the methods is also implemented. Version 1.1 and later also
implements the Poisson linear model with dinucleotide composition. Version
1.2 corrected a bug in expData.R. This bug leads to mis-labeled lines in
plotCoef.R, but will not change other parts like training, testing, or

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
%doc %{rlibdir}/mseq/html
%doc %{rlibdir}/mseq/DESCRIPTION
%{rlibdir}/mseq/R
%{rlibdir}/mseq/LICENSE
%{rlibdir}/mseq/Readme_format.txt
%{rlibdir}/mseq/data_top100_moved.txt
%{rlibdir}/mseq/INDEX
%{rlibdir}/mseq/data
%{rlibdir}/mseq/NAMESPACE
%{rlibdir}/mseq/help
%{rlibdir}/mseq/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora