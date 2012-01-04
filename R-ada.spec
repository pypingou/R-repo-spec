%global packname  ada
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          ada: an R package for stochastic boosting

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rpart 

BuildRequires:    R-devel tex(latex) R-rpart 

%description
Performs discrete, real, and gentle boost under both exponential and
logistic loss on a given data set.  The package ada provides a
straightforward, well-documented, and broad boosting routine for
classification, ideally suited for small to moderate-sized data sets. 
Please refer to the Url below for more information.

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
%doc %{rlibdir}/ada/DESCRIPTION
%doc %{rlibdir}/ada/html
%{rlibdir}/ada/help
%{rlibdir}/ada/Meta
%{rlibdir}/ada/data
%{rlibdir}/ada/INDEX
%{rlibdir}/ada/R
%{rlibdir}/ada/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora