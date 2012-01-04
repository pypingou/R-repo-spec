%global packname  textir
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Inverse Regression for Text Analysis

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-slam 

BuildRequires:    R-devel tex(latex) R-slam 

%description
A suite of tools for text and sentiment mining.  This includes the `mnlm'
function, for sparse multinomial logistic regression, `pls', a concise
partial least squares routine, and the `topics' function, for efficient
estimation and dimension selection in latent topic models.

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
%doc %{rlibdir}/textir/html
%doc %{rlibdir}/textir/DESCRIPTION
%doc %{rlibdir}/textir/CITATION
%{rlibdir}/textir/help
%{rlibdir}/textir/libs
%{rlibdir}/textir/Meta
%{rlibdir}/textir/data
%{rlibdir}/textir/R
%{rlibdir}/textir/LICENSE
%{rlibdir}/textir/NAMESPACE
%{rlibdir}/textir/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.1-1
- initial package for Fedora