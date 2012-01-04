%global packname  sharx
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Models and Data Sets for the Study of Species-Area Relationships

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Formula R-dclone 

BuildRequires:    R-devel tex(latex) R-Formula R-dclone 

%description
Data sets and SAR, SARX, HSAR and HSARX models as described in Solymos and
Lele (in press).

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
%doc %{rlibdir}/sharx/DESCRIPTION
%doc %{rlibdir}/sharx/COPYING
%doc %{rlibdir}/sharx/html
%doc %{rlibdir}/sharx/CITATION
%{rlibdir}/sharx/HISTORY
%{rlibdir}/sharx/sardata.txt
%{rlibdir}/sharx/sardata.bib
%{rlibdir}/sharx/Meta
%{rlibdir}/sharx/help
%{rlibdir}/sharx/INDEX
%{rlibdir}/sharx/data
%{rlibdir}/sharx/R
%{rlibdir}/sharx/ChangeLog
%{rlibdir}/sharx/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora