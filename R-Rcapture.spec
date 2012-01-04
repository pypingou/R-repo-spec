%global packname  Rcapture
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Loglinear Models for Capture-Recapture Experiments

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Estimation of abundance and other demographic parameters for closed
populations, open populations and the robust design in capture-recapture
experiments using loglinear models.

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
%doc %{rlibdir}/Rcapture/NEWS
%doc %{rlibdir}/Rcapture/html
%doc %{rlibdir}/Rcapture/DESCRIPTION
%doc %{rlibdir}/Rcapture/doc
%{rlibdir}/Rcapture/NAMESPACE
%{rlibdir}/Rcapture/Meta
%{rlibdir}/Rcapture/data
%{rlibdir}/Rcapture/INDEX
%{rlibdir}/Rcapture/R
%{rlibdir}/Rcapture/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora