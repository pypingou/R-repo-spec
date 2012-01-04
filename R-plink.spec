%global packname  plink
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          IRT Separate Calibration Linking Methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lattice 
Requires:         R-MASS R-statmod 

BuildRequires:    R-devel tex(latex) R-methods R-lattice
BuildRequires:    R-MASS R-statmod 


%description
This package uses item response theory methods to compute linking
constants and conduct chain linking of unidimensional or multidimensional
tests for multiple groups under a common item design.  The unidimensional
methods include the Mean/Mean, Mean/Sigma, Haebara, and Stocking-Lord
methods for dichotomous (1PL, 2PL and 3PL) and/or polytomous (graded
response, partial credit/generalized partial credit, nominal, and
multiple-choice model) items.  The multidimensional methods include the
least squares method and extensions of the Haebara and Stocking-Lord
method using single or multiple dilation parameters for multidimensional
extensions of all the unidimensional dichotomous and polytomous item
response models.  The package also includes functions for importing item
and/or ability parameters from common IRT software, conducting IRT true
score and observed score equating, and plotting item response
curves/surfaces, vector plots, and comparison plots for examining
parameter drift.

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
%doc %{rlibdir}/plink/NEWS
%doc %{rlibdir}/plink/CITATION
%doc %{rlibdir}/plink/doc
%doc %{rlibdir}/plink/DESCRIPTION
%doc %{rlibdir}/plink/html
%{rlibdir}/plink/NAMESPACE
%{rlibdir}/plink/Meta
%{rlibdir}/plink/INDEX
%{rlibdir}/plink/R
%{rlibdir}/plink/help
%{rlibdir}/plink/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora