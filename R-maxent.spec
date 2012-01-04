%global packname  maxent
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Low-memory Multinomial Logistic Regression with Support for Text Classification

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Rcpp R-SparseM R-tm 


BuildRequires:    R-devel tex(latex) R-methods R-Rcpp R-SparseM R-tm



%description
maxent is an R package with tools for low-memory multinomial logistic
regression, also known as maximum entropy. The focus of this maximum
entropy classifier is to minimize memory consumption on very large
datasets, particularly sparse document-term matrices represented by the tm

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora