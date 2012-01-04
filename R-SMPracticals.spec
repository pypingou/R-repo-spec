%global packname  SMPracticals
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Practicals for use with Davison (2003) Statistical Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ellipse 

BuildRequires:    R-devel tex(latex) R-ellipse 

%description
This package contains the datasets and a few functions for use with the
practicals outlined in Appendix A of the book Statistical Models (Davison,
2003, Cambridge University Press). The practicals themselves can be found
at http://statwww.epfl.ch/davison/SM/

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
%doc %{rlibdir}/SMPracticals/DESCRIPTION
%doc %{rlibdir}/SMPracticals/html
%{rlibdir}/SMPracticals/Meta
%{rlibdir}/SMPracticals/INDEX
%{rlibdir}/SMPracticals/R
%{rlibdir}/SMPracticals/help
%{rlibdir}/SMPracticals/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora