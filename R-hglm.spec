%global packname  hglm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Hierarchical Generalized Linear Models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-MASS 

BuildRequires:    R-devel tex(latex) R-Matrix R-MASS 

%description
The hglm package is used to fit hierarchical generalized linear models. It
can be used for linear mixed models and generalized linear mixed models
with random effects for a variety of links and a variety of distributions
for both the outcomes and the random effects. Fixed effects can also be
fitted in the dispersion part of the mean model.

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
%doc %{rlibdir}/hglm/CITATION
%doc %{rlibdir}/hglm/doc
%doc %{rlibdir}/hglm/DESCRIPTION
%doc %{rlibdir}/hglm/html
%{rlibdir}/hglm/help
%{rlibdir}/hglm/INDEX
%{rlibdir}/hglm/Meta
%{rlibdir}/hglm/data
%{rlibdir}/hglm/R
%{rlibdir}/hglm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora