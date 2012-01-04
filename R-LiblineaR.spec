%global packname  LiblineaR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.80.4
Release:          1%{?dist}
Summary:          Linear Predictive Models Based On The Liblinear C/C++ Library.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.80-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This R package is a wrapper around the liblinear C/C++ library for machine
learning. LIBLINEAR is a linear classifier for data with millions of
instances and features. It supports L2-regularized classifiers (such as
L2-loss linear SVM, L1-loss linear SVM, and logistic regression) as well
as L1-regularized classifiers (such as L2-loss linear SVM and logistic
regression). The main features of LiblineaR include multi-class
classification (one-vs-the rest, and Crammer & Singer method), cross
validation for model selection, probability estimates (logistic regression
only) or weights for unbalanced data. The estimation of the models is
particularly fast as compared to other libraries. For more information on
the C/C++ liblinear library itself, refer to R.-E. Fan, K.-W. Chang, C.-J.
Hsieh, X.-R. Wang, and C.-J. Lin. LIBLINEAR: A Library for Large Linear
Classification, Journal of Machine Learning Research 9(2008), 1871-1874,
available at http://www.csie.ntu.edu.tw/~cjlin/liblinear . The two first
blocks of the package version indicates which version of liblinear is
currently supported. For example: 1.32-14 means that the package supports
the version 1.32 of liblinear.

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
%doc %{rlibdir}/LiblineaR/CITATION
%doc %{rlibdir}/LiblineaR/html
%doc %{rlibdir}/LiblineaR/NEWS
%doc %{rlibdir}/LiblineaR/DESCRIPTION
%{rlibdir}/LiblineaR/R
%{rlibdir}/LiblineaR/libs
RPM build errors:
%{rlibdir}/LiblineaR/NAMESPACE
%{rlibdir}/LiblineaR/help
%{rlibdir}/LiblineaR/Meta
%{rlibdir}/LiblineaR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.80.4-1
- initial package for Fedora