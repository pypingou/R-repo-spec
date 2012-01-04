%global packname  tmvtnorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Truncated Multivariate Normal and Student t Distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-utils R-stats4 R-gmm 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-utils R-stats4 R-gmm 

%description
Random number generation for the truncated multivariate normal and Student
t distribution. Computes probabilities, quantiles and densities, including
one-dimensional and bivariate marginal densities. Computes first and
second moments (i.e. mean and covariance matrix) for the double-truncated
multinormal case.

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
%doc %{rlibdir}/tmvtnorm/DESCRIPTION
%doc %{rlibdir}/tmvtnorm/html
%doc %{rlibdir}/tmvtnorm/CITATION
%doc %{rlibdir}/tmvtnorm/NEWS
%{rlibdir}/tmvtnorm/R
%{rlibdir}/tmvtnorm/user-feedback.txt
%{rlibdir}/tmvtnorm/help
%{rlibdir}/tmvtnorm/INDEX
%{rlibdir}/tmvtnorm/demo
%{rlibdir}/tmvtnorm/Meta
%{rlibdir}/tmvtnorm/libs
%{rlibdir}/tmvtnorm/NAMESPACE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora