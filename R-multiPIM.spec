%global packname  multiPIM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Variable Importance Analysis with Population Intervention Models

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lars R-penalized R-polspline R-rpart 

BuildRequires:    R-devel tex(latex) R-lars R-penalized R-polspline R-rpart 

%description
Performs variable importance analysis for possibly many exposures of
interest and possibly many outcomes of interest. This is done by fitting
Population Intervention Models. The default is to use a Targeted Maximum
Likelihood Estimator (TMLE). The other available estimators are Inverse
Probability of Censoring Weighted (IPCW), Double-Robust IPCW (DR-IPCW),
and Graphical Computation (G-COMP) estimators. Inference can be obtained
from the influence curve (plug-in) or by bootstrapping.

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
%doc %{rlibdir}/multiPIM/html
%doc %{rlibdir}/multiPIM/DESCRIPTION
%{rlibdir}/multiPIM/R
%{rlibdir}/multiPIM/NAMESPACE
%{rlibdir}/multiPIM/help
%{rlibdir}/multiPIM/INDEX
%{rlibdir}/multiPIM/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora