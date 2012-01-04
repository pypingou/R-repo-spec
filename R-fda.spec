%global packname  fda
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.7
Release:          1%{?dist}
Summary:          Functional Data Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-zoo 

BuildRequires:    R-devel tex(latex) R-splines R-zoo 

%description
These functions were developed to support functional data analysis as
described in Ramsay, J. O. and Silverman, B. W. (2005) Functional Data
Analysis. New York: Springer.  They were ported from earlier versions in
Matlab and S-PLUS.  An introduction appears in Ramsay, J. O., Hooker,
Giles, and Graves, Spencer (2009) Functional Data Analysis with R and
Matlab (Springer). The package includes data sets and script files working
many examples including all but one of the 76 figures in this latter book.
The principal changes to version 2.2.6 are: 1.  Major enhancements to
function smooth.basis as well as the functions that call it.  New or
revised arguments are: "wtvec" may now be a positive symmetric matrix as
well as a vector "covariates" for inputting covariate matrices that
explain some fraction of the data to be smoothed (often called
"semiparametric smoothing") "method=qr" enables an algorithm based on the
qr- decomposition that will be more accurate than the usual approach
relying on the Choleski decomposition. It will, however, be slower. 2. 
Greatly expanded examples in the smooth.basis.Rd file that show a wider
range of uses of this function. 3.  Function data2fd has been replaced by
function Data2fd for simple smoothing problems.  Data2fd is designed to be
invoked with various argument configurations. 4.  And the usual fixes of
reported bugs, especially in the registraton functions, landmarkreg and

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
%doc %{rlibdir}/fda/DESCRIPTION
%doc %{rlibdir}/fda/doc
%doc %{rlibdir}/fda/html
%doc %{rlibdir}/fda/NEWS
%{rlibdir}/fda/originals
%{rlibdir}/fda/help
%{rlibdir}/fda/data
%{rlibdir}/fda/Meta
%{rlibdir}/fda/R
%{rlibdir}/fda/demo
%{rlibdir}/fda/Matlab
%{rlibdir}/fda/INDEX
%{rlibdir}/fda/NAMESPACE
%{rlibdir}/fda/scripts

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.7-1
- initial package for Fedora