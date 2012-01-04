%global packname  partykit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A Toolkit for Recursive Partytioning

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-grid 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-grid 

%description
A toolkit with infrastructure for representing, summarizing, and
visualizing tree-structured regression and classification models. This
unified infrastructure can be used for reading/coercing tree models from
different sources (rpart, RWeka, PMML) yielding objects that share
functionality for print/plot/predict methods. (It will also be the basis
for a re-implementation of the party package. Currently, only a
re-implementation of ctree() is contained in the package.)

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
%doc %{rlibdir}/partykit/doc
%doc %{rlibdir}/partykit/NEWS
%doc %{rlibdir}/partykit/DESCRIPTION
%doc %{rlibdir}/partykit/html
%{rlibdir}/partykit/INDEX
%{rlibdir}/partykit/R
%{rlibdir}/partykit/pmml
%{rlibdir}/partykit/NAMESPACE
%{rlibdir}/partykit/data
%{rlibdir}/partykit/Meta
%{rlibdir}/partykit/help
%{rlibdir}/partykit/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora