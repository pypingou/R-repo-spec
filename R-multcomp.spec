%global packname  multcomp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          Simultaneous Inference in General Parametric Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-mvtnorm R-survival 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-mvtnorm R-survival 

%description
Simultaneous tests and confidence intervals for general linear hypotheses
in parametric models, including linear, generalized linear, linear mixed
effects, and survival models. The package includes demos reproducing
analyzes presented in the book "Multiple Comparisons Using R" (Bretz,
Hothorn, Westfall, 2010, CRC Press).

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
%doc %{rlibdir}/multcomp/doc
%doc %{rlibdir}/multcomp/DESCRIPTION
%doc %{rlibdir}/multcomp/NEWS
%doc %{rlibdir}/multcomp/CITATION
%doc %{rlibdir}/multcomp/html
%{rlibdir}/multcomp/R
%{rlibdir}/multcomp/demo
%{rlibdir}/multcomp/INDEX
%{rlibdir}/multcomp/NAMESPACE
%{rlibdir}/multcomp/help
%{rlibdir}/multcomp/MCMT
%{rlibdir}/multcomp/applications
%{rlibdir}/multcomp/Meta
%{rlibdir}/multcomp/multcomp_VA.R
%{rlibdir}/multcomp/multcomp_coxme.R
%{rlibdir}/multcomp/data
%{rlibdir}/multcomp/deprecated
%{rlibdir}/multcomp/CHANGES

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.8-1
- initial package for Fedora