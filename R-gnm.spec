%global packname  gnm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Generalized Nonlinear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-MASS R-stats R-graphics R-Matrix R-nnet R-qvcalc R-relimp 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-MASS R-stats R-graphics R-Matrix R-nnet R-qvcalc R-relimp 


%description
Functions to specify and fit generalized nonlinear models, including
models with multiplicative interaction terms such as the UNIDIFF model
from sociology and the AMMI model from crop science, and many others. 
Over-parameterized representations of models are used throughout;
functions are provided for inference on estimable parameter combinations,
as well as standard methods for diagnostics etc.

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
%doc %{rlibdir}/gnm/html
%doc %{rlibdir}/gnm/NEWS
%doc %{rlibdir}/gnm/DESCRIPTION
%doc %{rlibdir}/gnm/CITATION
%doc %{rlibdir}/gnm/doc
%{rlibdir}/gnm/NAMESPACE
%{rlibdir}/gnm/Meta
%{rlibdir}/gnm/libs
%{rlibdir}/gnm/help
%{rlibdir}/gnm/R
%{rlibdir}/gnm/demo
%{rlibdir}/gnm/data
%{rlibdir}/gnm/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora