%global packname  klausuR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.12.2
Release:          1%{?dist}
Summary:          Multiple Choice Test Evaluation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.12-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xtable R-psychometric R-methods R-graphics R-tools 

BuildRequires:    R-devel tex(latex) R-xtable R-psychometric R-methods R-graphics R-tools 

%description
A set of functions designed to quickly generate results of a multiple
choice test. Generates detailed global results, lists for anonymous
feedback and personalised result feedback (in LaTeX and/or PDF format), as
well as item statistics like Cronbach's alpha or disciminatory power.

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.12.2-1
- initial package for Fedora