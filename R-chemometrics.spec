%global packname  chemometrics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          Multivariate Statistical Analysis in Chemometrics

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-class R-e1071 R-gclus R-lars R-MASS R-mclust R-nnet R-pcaPP R-pls R-rpart R-robustbase R-som 

BuildRequires:    R-devel tex(latex) R-class R-e1071 R-gclus R-lars R-MASS R-mclust R-nnet R-pcaPP R-pls R-rpart R-robustbase R-som 

%description
This package is the R companion to the book "Introduction to Multivariate
Statistical Analysis in Chemometrics" written by K. Varmuza and P.
Filzmoser (2009)

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.7-1
- initial package for Fedora