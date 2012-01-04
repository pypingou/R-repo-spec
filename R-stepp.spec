%global packname  stepp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Subpopulation Treatment Effect Pattern Plot (STEPP)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cmprsk R-survival R-splines 

BuildRequires:    R-devel tex(latex) R-cmprsk R-survival R-splines 

%description
A method to explore the treatment-covariate interactions in survival data
arising from two treatment arms of a clinical trial.  A permutation
distribution approach to inference is implemented, based on permuting the
covariate values within each treatment group.

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
%doc %{rlibdir}/stepp/html
%doc %{rlibdir}/stepp/DESCRIPTION
%{rlibdir}/stepp/INDEX
%{rlibdir}/stepp/R
%{rlibdir}/stepp/help
%{rlibdir}/stepp/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.2-1
- initial package for Fedora