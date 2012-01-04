%global packname  ElemStatLearn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7.1
Release:          1%{?dist}
Summary:          Data sets, functions and examples from the book: "The Elements of Statistical Learning, Data Mining, Inference, and Prediction" by Trevor Hastie, Robert Tibshirani and Jerome Friedman.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Useful when reading the book above mentioned, in the documentation
referred to as `the book'.

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
%doc %{rlibdir}/ElemStatLearn/html
%doc %{rlibdir}/ElemStatLearn/DESCRIPTION
%{rlibdir}/ElemStatLearn/help
%{rlibdir}/ElemStatLearn/data
%{rlibdir}/ElemStatLearn/INDEX
%{rlibdir}/ElemStatLearn/R
%{rlibdir}/ElemStatLearn/Meta
%{rlibdir}/ElemStatLearn/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7.1-1
- initial package for Fedora