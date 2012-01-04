%global packname  fechner
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Fechnerian Scaling of Discrete Object Sets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-base R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-base R-graphics R-stats 

%description
Functions and example datasets for Fechnerian scaling of discrete object
sets.  It computes Fechnerian distances among objects representing
subjective dissimilarities, and other related information.  See
package?fechner for an overview.

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
%doc %{rlibdir}/fechner/CITATION
%doc %{rlibdir}/fechner/DESCRIPTION
%doc %{rlibdir}/fechner/NEWS
%doc %{rlibdir}/fechner/doc
%doc %{rlibdir}/fechner/html
%{rlibdir}/fechner/INDEX
%{rlibdir}/fechner/data
%{rlibdir}/fechner/Meta
%{rlibdir}/fechner/R
%{rlibdir}/fechner/NAMESPACE
%{rlibdir}/fechner/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora